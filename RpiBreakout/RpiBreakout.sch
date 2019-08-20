EESchema Schematic File Version 4
LIBS:RpiBreakout-cache
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:Raspberry_Pi_2_3 J1
U 1 1 5D4D3AFF
P 5050 4150
F 0 "J1" H 5050 5631 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 5050 5540 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_2x20_P2.54mm_Vertical" H 5050 4150 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf" H 5050 4150 50  0001 C CNN
	1    5050 4150
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x03_Female J2
U 1 1 5D4D5BF9
P 3250 2850
F 0 "J2" H 3278 2876 50  0000 L CNN
F 1 "Conn_01x03_Female" H 3278 2785 50  0000 L CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x03_P2.54mm_Vertical" H 3250 2850 50  0001 C CNN
F 3 "~" H 3250 2850 50  0001 C CNN
	1    3250 2850
	1    0    0    -1  
$EndComp
Wire Wire Line
	4650 5450 4750 5450
Connection ~ 4750 5450
Wire Wire Line
	4750 5450 4850 5450
Connection ~ 4850 5450
Wire Wire Line
	4850 5450 4950 5450
Connection ~ 4950 5450
Wire Wire Line
	4950 5450 5050 5450
Connection ~ 5050 5450
Wire Wire Line
	5050 5450 5150 5450
Connection ~ 5150 5450
Wire Wire Line
	5150 5450 5250 5450
Connection ~ 5250 5450
Wire Wire Line
	5250 5450 5350 5450
Wire Wire Line
	5350 5450 5350 6050
Connection ~ 5350 5450
$Comp
L power:GND #PWR0101
U 1 1 5D4D712F
P 5350 6050
F 0 "#PWR0101" H 5350 5800 50  0001 C CNN
F 1 "GND" H 5355 5877 50  0000 C CNN
F 2 "" H 5350 6050 50  0001 C CNN
F 3 "" H 5350 6050 50  0001 C CNN
	1    5350 6050
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0102
U 1 1 5D4D733C
P 4850 2500
F 0 "#PWR0102" H 4850 2350 50  0001 C CNN
F 1 "+5V" H 4865 2673 50  0000 C CNN
F 2 "" H 4850 2500 50  0001 C CNN
F 3 "" H 4850 2500 50  0001 C CNN
	1    4850 2500
	1    0    0    -1  
$EndComp
Wire Wire Line
	4950 2850 4850 2850
Wire Wire Line
	4850 2500 4850 2850
Connection ~ 4850 2850
$Comp
L power:+3.3V #PWR0103
U 1 1 5D4D8269
P 5150 2500
F 0 "#PWR0103" H 5150 2350 50  0001 C CNN
F 1 "+3.3V" H 5165 2673 50  0000 C CNN
F 2 "" H 5150 2500 50  0001 C CNN
F 3 "" H 5150 2500 50  0001 C CNN
	1    5150 2500
	1    0    0    -1  
$EndComp
Wire Wire Line
	5150 2500 5150 2850
Wire Wire Line
	5250 2850 5150 2850
Connection ~ 5150 2850
$Comp
L power:+5V #PWR0104
U 1 1 5D4D9932
P 2700 2750
F 0 "#PWR0104" H 2700 2600 50  0001 C CNN
F 1 "+5V" H 2715 2923 50  0000 C CNN
F 2 "" H 2700 2750 50  0001 C CNN
F 3 "" H 2700 2750 50  0001 C CNN
	1    2700 2750
	1    0    0    -1  
$EndComp
Wire Wire Line
	2700 2750 3050 2750
$Comp
L power:GND #PWR0105
U 1 1 5D4DA21F
P 2700 3000
F 0 "#PWR0105" H 2700 2750 50  0001 C CNN
F 1 "GND" H 2705 2827 50  0000 C CNN
F 2 "" H 2700 3000 50  0001 C CNN
F 3 "" H 2700 3000 50  0001 C CNN
	1    2700 3000
	1    0    0    -1  
$EndComp
Wire Wire Line
	3050 2950 2700 2950
Wire Wire Line
	2700 2950 2700 3000
Wire Wire Line
	2850 3750 2850 2850
Wire Wire Line
	2850 2850 3050 2850
Text Label 3150 3750 0    50   ~ 0
LED
Wire Wire Line
	2850 3750 4250 3750
$Comp
L Connector:Conn_01x06_Female J3
U 1 1 5D4E782F
P 7150 3650
F 0 "J3" H 7100 3200 50  0000 L CNN
F 1 "Conn_01x06_Female" H 7200 3100 50  0000 L CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x06_P2.54mm_Vertical" H 7150 3650 50  0001 C CNN
F 3 "~" H 7150 3650 50  0001 C CNN
	1    7150 3650
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR0106
U 1 1 5D4E9B11
P 6400 3450
F 0 "#PWR0106" H 6400 3300 50  0001 C CNN
F 1 "+3.3V" H 6415 3623 50  0000 C CNN
F 2 "" H 6400 3450 50  0001 C CNN
F 3 "" H 6400 3450 50  0001 C CNN
	1    6400 3450
	1    0    0    -1  
$EndComp
Wire Wire Line
	6400 3450 6950 3450
$Comp
L power:GND #PWR0107
U 1 1 5D4EA3CD
P 6850 4200
F 0 "#PWR0107" H 6850 3950 50  0001 C CNN
F 1 "GND" H 6855 4027 50  0000 C CNN
F 2 "" H 6850 4200 50  0001 C CNN
F 3 "" H 6850 4200 50  0001 C CNN
	1    6850 4200
	1    0    0    -1  
$EndComp
Text Label 6200 3650 0    50   ~ 0
SCL
Text Label 6200 3550 0    50   ~ 0
SDA
Wire Wire Line
	5850 3550 6950 3550
Wire Wire Line
	5850 3650 6950 3650
Wire Wire Line
	6950 3850 6850 3850
Wire Wire Line
	6850 3850 6850 4200
Text Notes 7250 3450 0    50   ~ 0
red
Text Notes 7250 3550 0    50   ~ 0
yellow
Text Notes 7250 3650 0    50   ~ 0
green
Text Notes 7250 3850 0    50   ~ 0
black
Text Notes 7250 3750 0    50   ~ 0
orange
Text Notes 7250 3950 0    50   ~ 0
brown
Wire Notes Line
	7550 3400 8700 3400
Wire Notes Line
	7550 3500 8700 3500
Wire Notes Line
	7550 3600 8700 3600
Wire Notes Line
	7550 3700 8700 3700
Wire Notes Line
	7550 3800 8700 3800
Wire Notes Line
	7550 3900 8700 3900
Text Notes 8850 3550 0    50   ~ 0
yellow
Text Notes 8850 3650 0    50   ~ 0
green
Text Notes 8850 3400 0    50   ~ 0
gray
Text Notes 8850 3850 0    50   ~ 0
purple
Text Notes 8850 3950 0    50   ~ 0
Blue
NoConn ~ 8750 3700
Text Label 3700 3650 0    50   ~ 0
shutdown
Wire Wire Line
	3700 3650 4250 3650
Text Label 6400 3950 0    50   ~ 0
shutdown
Wire Wire Line
	6400 3950 6950 3950
$EndSCHEMATC
