# Fix angles that are *just* within range

import mpmath


class TrigEquivAngle():
    mpmath.mp.pretty = True

    def equiv_sin(x,range1,range2,radians=None,degrees=None,accuracy=2):
        mpmath.mp.dps = accuracy + 1
        range1, range2 = TrigEquivAngle.deg_or_rad([range1,range2], degrees)
        firstSinAngle = mpmath.asin(x)
        secondSinAngle = mpmath.pi - firstSinAngle

        angles = TrigEquivAngle.create_equiv_angle_list([firstSinAngle,secondSinAngle],range1,range2,2*mpmath.pi)
        return(TrigEquivAngle.clean_angles_rad_deg(angles,radians,degrees,accuracy))

    def equiv_cos(x,range1,range2,radians=None,degrees=None,accuracy=2):
        mpmath.mp.dps = accuracy + 1
        range1, range2 = TrigEquivAngle.deg_or_rad([range1,range2], degrees)
        firstCosAngle = mpmath.acos(x)
        secondCosAngle = 2*mpmath.pi - firstCosAngle

        angles = TrigEquivAngle.create_equiv_angle_list([firstCosAngle,secondCosAngle],range1,range2,2*mpmath.pi)
        return(TrigEquivAngle.clean_angles_rad_deg(angles,radians,degrees,accuracy))

    def equiv_tan(x,range1,range2,radians=None,degrees=None,accuracy=2):
        mpmath.mp.dps = accuracy + 1
        range1, range2 = TrigEquivAngle.deg_or_rad([range1,range2], degrees)
        firstTanAngle = mpmath.atan(x)

        angles = TrigEquivAngle.create_equiv_angle_list([firstTanAngle],range1,range2,mpmath.pi)
        return(TrigEquivAngle.clean_angles_rad_deg(angles,radians,degrees,accuracy))

    def equiv_cosec(x,range1,range2,radians=None,degrees=None,accuracy=2):
        return TrigEquivAngle.equiv_sin(1/x,range1,range2,radians,degrees,accuracy)

    def equiv_sec(x,range1,range2,radians=None,degrees=None,accuracy=2):
        return TrigEquivAngle.equiv_cos(1/x,range1,range2,radians,degrees,accuracy)

    def equiv_cot(x,range1,range2,radians=None,degrees=None,accuracy=2):
        return TrigEquivAngle.equiv_tan(1/x,range1,range2,radians,degrees,accuracy)

    def deg_or_rad(angles, degrees):
        for i in angles:
            if degrees is True:
                angles[angles.index(i)] = mpmath.radians(i)
        return angles

    def create_equiv_angle_list(angles,range1,range2,plusminusnum):
        returnlist=[]
        z = 0
        for i in angles:
            x = i
            y = i
            returnlist.append(i)

            if i < range1 : del returnlist[z]
            if i > range2 : del returnlist[z]
            z += 1

            while True:
                if (x - plusminusnum) > range1:
                    x -= plusminusnum
                    returnlist.append(x)
                else:
                    break
            while True:
                if (y + plusminusnum) < range2:
                    y += plusminusnum
                    returnlist.append(y)
                else:
                    break

        return returnlist

    def clean_angles_rad_deg(angles,radians,degrees,accuracy):
        x = 0
        if degrees is True:
            for i in angles:
                angles[x] = mpmath.degrees(i)
                x += 1

        for i in angles:
            if angles.count(i) > 1:
                angles.remove(i)

        angles.sort()
        return angles
