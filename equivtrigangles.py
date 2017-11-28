#Fix angles that are *just* within range

import mpmath
import math

class TrigEquivAngle():
    mpmath.mp.pretty = True

    def equiv_sin(x,range1,range2,radians=None,degrees=None,accuracy=2):
        range1,range2 = TrigEquivAngle.check_deg_range(range1,range2,degrees)
        firstSinAngle = math.asin(x)
        firstSinAngle1 = firstSinAngle
        secondSinAngle = mpmath.pi - firstSinAngle
        secondSinAngle1 = secondSinAngle
        angles = TrigEquivAngle.create_equiv_angle_list([firstSinAngle,secondSinAngle],range1,range2,2*mpmath.pi)
        return(TrigEquivAngle.clean_angles_rad_deg(angles,radians,degrees,accuracy))
    
    def next_sin(x,radians=None,degrees=None):
        angle, range1, range2 = TrigEquivAngle.next_func(x,radians=radians,degrees=degrees)
        angles = TrigEquivAngle.equiv_sin(angle,range1,range2,radians=radians,degrees=degrees)
        return TrigEquivAngle.return_next_angle(x,angles)

    def equiv_cos(x,range1,range2,radians=None,degrees=None,accuracy=2):
        range1,range2 = TrigEquivAngle.check_deg_range(range1,range2,degrees)
        firstCosAngle = mpmath.acos(x)
        firstCosAngle1 = firstCosAngle
        secondCosAngle = 2*mpmath.pi - firstCosAngle
        secondCosAngle1 = secondCosAngle
        angles = TrigEquivAngle.create_equiv_angle_list([firstCosAngle,secondCosAngle],range1,range2,2*mpmath.pi)
        return(TrigEquivAngle.clean_angles_rad_deg(angles,radians,degrees,accuracy))

    def next_cos(x,radians=None,degrees=None):
        angle, range1, range2 = TrigEquivAngle.next_func(x,radians=radians,degrees=degrees)
        angles = TrigEquivAngle.equiv_cos(angle,range1,range2,radians=radians,degrees=degrees)
        return TrigEquivAngle.return_next_angle(x,angles)

    def equiv_tan(x,range1,range2,radians=None,degrees=None,accuracy=2):
        range1,range2 = TrigEquivAngle.check_deg_range(range1,range2,degrees)
        firstTanAngle = mpmath.atan(x)
        secondTanAngle = firstTanAngle
        angles = TrigEquivAngle.create_equiv_angle_list([firstTanAngle],range1,range2,mpmath.pi)
        return(TrigEquivAngle.clean_angles_rad_deg(angles,radians,degrees,accuracy))

    def next_tan(x,radians=None,degrees=None):
        angle, range1, range2 = TrigEquivAngle.next_func(x,radians=radians,degrees=degrees)
        angles = TrigEquivAngle.equiv_tan(angle,range1,range2,radians=radians,degrees=degrees)
        return TrigEquivAngle.return_next_angle(x,angles)

    def equiv_cosec(x,range1,range2,radians=None,degrees=None,accuracy=2):
        return TrigEquivAngle.equiv_sin(1/x,range1,range2,radians,degrees,accuracy)

    def next_cosec(x,radians=None,degrees=None):
        angle, range1, range2 = TrigEquivAngle.next_func(x,radians=radians,degrees=degrees)
        angles = TrigEquivAngle.equiv_cosec(angle,range1,range2,radians=radians,degrees=degrees)
        return TrigEquivAngle.return_next_angle(x,angles)

    def equiv_sec(x,range1,range2,radians=None,degrees=None,accuracy=2):
        return TrigEquivAngle.equiv_cos(1/x,range1,range2,radians,degrees,accuracy)

    def next_sec(x,radians=None,degrees=None):
        angle, range1, range2 = TrigEquivAngle.next_func(x,radians=radians,degrees=degrees)
        angles = TrigEquivAngle.equiv_sec(angle,range1,range2,radians=radians,degrees=degrees)
        return TrigEquivAngle.return_next_angle(x,angles)

    def equiv_cot(x,range1,range2,radians=None,degrees=None,accuracy=2):
        return TrigEquivAngle.equiv_tan(1/x,range1,range2,radians,degrees,accuracy)

    def next_cot(x,radians=None,degrees=None):
        angle, range1, range2 = TrigEquivAngle.next_func(x,radians=radians,degrees=degrees)
        angles = TrigEquivAngle.equiv_cot(angle,range1,range2,radians=radians,degrees=degrees)
        return TrigEquivAngle.return_next_angle(x,angles)

    def next_func(x,radians=None,degrees=None):
        if radians is True:
            angle = mpmath.sin(x)
            range1, range2 = x - 2*mpmath.pi, x + 2*mpmath.pi
        elif degrees is True:
            angle = mpmath.sin(mpmath.radians(x))
            range1, range2 = x - 360, x + 360
        return angle, range1, range2

    def return_next_angle(x,angles):
        index = angles.index(x)
        return angles[index+1]

    def check_deg_range(range1,range2,degrees):
        if degrees is True:
            range1 = mpmath.radians(range1)
            range2 = mpmath.radians(range2)
            return range1,range2
        else:
            return range1,range2

    def create_equiv_angle_list(angles,range1,range2,plusminusnum):
        returnlist=[]
        z = 0
        for i in angles:
            x=i
            y=i
            returnlist.append(i)

            if i < range1:del returnlist[z]
            if i > range2:del returnlist[z]         
            z+=1

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
        angles.sort()
        x = 0
        if degrees is True:
            for i in angles:
                angles[x] = round(mpmath.degrees(i),accuracy)
                x+=1
        
        elif radians is True:
            for i in angles:
                angles[x] = round(i, accuracy)
                x+=1
        
        return angles