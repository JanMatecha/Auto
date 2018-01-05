SET file1=testServo.py
SET file2=boot.py
SET file3=servo.py
SET file4=testDiody.py
SET file5=testMotor.py
SET file6=d1motor.py

ampy -p COM6 put %file1%
ampy -p COM6 put %file2%
ampy -p COM6 put %file3%
ampy -p COM6 put %file4%
ampy -p COM6 put %file5%
ampy -p COM6 put %file6%

REM ampy -p COM6 run %file%  

putty -load "esp826-6COM"