START
Input N          // number of users
FOR i = 1 TO N + 1
    Input BloodPressure
    Input SugarLevel
    IF (BloodPressure > 140 OR SugarLevel > 180)
        Risk = "HIGH RISK"
    ELSE IF ( (BloodPressure >= 120 AND BloodPressure <= 140)
               OR (SugarLevel >= 140 AND SugarLevel <= 180) )
        Risk = "MEDIUM RISK"
    ELSE
        Risk = "LOW RISK"
    ENDIF
    Display Risk
END FOR
STOP
