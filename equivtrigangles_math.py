#working out cosec, sec and tan is buggy 

import math

class TrigEquivAngle():

    def equiv_sin(x,range1,range2,radians=None,degrees=True,accuracy=2):
        firstSinAngle = math.degrees(math.asin(x))
        firstSinAngle1 = firstSinAngle
        secondSinAngle = 180 - firstSinAngle
        secondSinAngle1 = secondSinAngle

        angles = TrigEquivAngle.create_equiv_angle_list([firstSinAngle,secondSinAngle],range1,range2,360)
        return(TrigEquivAngle.clean_angles_rad_deg(angles,radians,degrees,accuracy))

    def equiv_cos(x,range1,range2,radians=None,degrees=True,accuracy=2):
        firstCosAngle = math.degrees(math.acos(x))
        firstCosAngle1 = firstCosAngle
        secondCosAngle = 360 - firstCosAngle
        secondCosAngle1 = secondCosAngle

        angles = TrigEquivAngle.create_equiv_angle_list([firstCosAngle,secondCosAngle],range1,range2,360)
        return(TrigEquivAngle.clean_angles_rad_deg(angles,radians,degrees,accuracy))

    def equiv_tan(x,range1,range2,radians=None,degrees=True,accuracy=2):
        firstTanAngle = math.degrees(math.atan(x))
        secondTanAngle = firstTanAngle

        angles = TrigEquivAngle.create_equiv_angle_list([firstTanAngle],range1,range2,180)
        return(TrigEquivAngle.clean_angles_rad_deg(angles,radians,degrees,accuracy))

    def equiv_cosec(x,range1,range2,radians=None,degrees=True,accuracy=2):
        return TrigEquivAngle.recip_angles_list(TrigEquivAngle.equiv_sin(x,range1,range2,radians,degrees,accuracy),accuracy)

    def equiv_sec(x,range1,range2,radians=None,degrees=True,accuracy=2):
        return TrigEquivAngle.recip_angles_list(TrigEquivAngle.equiv_cos(x,range1,range2,radians,degrees,accuracy),accuracy)

    def equiv_cot(x,range1,range2,radians=None,degrees=True,accuracy=2):
        return TrigEquivAngle.recip_angles_list(TrigEquivAngle.equiv_tan(x,range1,range2,radians,degrees,accuracy),accuracy)

    def create_equiv_angle_list(angles,range1,range2,plusminusnum):
        returnlist=[]
        for i in angles:
            x=i
            y=i
            returnlist.append(i)

            while True:
                if (x - plusminusnum) > range1:
                    x -= 360
                    returnlist.append(x)
                else:
                    break

            while True:
                if (y + plusminusnum) < range2:
                    y += 360
                    returnlist.append(y)
                else:
                    break

        return returnlist

    def recip_angles_list(angles,accuracy):
        x=0
        for i in angles:
            angles[x] = round(1/i,accuracy)
            x+=1
        return angles
    
    def clean_angles_rad_deg(angles,radians,degrees,accuracy):
        angles.sort()
        x = 0

        if radians is True:
            for i in angles:
                angles[x] = round(math.radians(i),accuracy)
                x+=1
        
        elif degrees is True:
            for i in angles:
                angles[x] = round(i, accuracy)
                x+=1
            
        return angles