# Argyll CMS Notes

## SRGB

### White Point:
D65
6503.51K
x = 0.3127
y = 0.3290

## Argyll options

```-w x,y``` 
Set the target white point as chromaticity coordinates

```-t [temp]``` White Daylight locus target

```-I b|w```
Drift compensation, Black: ```-Ib```, White: ```-Iw```, Both: ```-Ibw```

```-d n``` choose display number

```-H``` high resolution mode

```-Q observ``` Observer: ```2012_2``` 

## Argyll Commands

```
dispcal -X ccxxdpt94-horiz-05-16T16:14.ccmx -v -t 6503.51 -Ibw -H -Q 2012_2 -o argyll-horiz-05-16T16:28
```

## monitor rgb
Vertical: 99 96 97q




## CCXX

```
ccxxmake -t l -v -H -o 2012_2 ccxxdpt94-05-16T16:14.ccmx
```

date +%F_%T   