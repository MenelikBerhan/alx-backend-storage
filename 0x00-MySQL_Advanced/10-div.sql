/*
 Creates a function `SafeDiv` that divides (and returns) the first by
 the second number or returns 0 if the second number is equal to 0.
 
 The function  takes 2 arguments: `a`, INT and `b`, INT
 And returns `a / b` or 0 if `b == 0`.
 */
-- create a function with above specification
CREATE FUNCTION SafeDiv(num1 INT, num2 INT)
RETURNS FLOAT DETERMINISTIC
    RETURN IF(num2 = 0, 0, num1 / num2);
