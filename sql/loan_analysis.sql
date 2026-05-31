-- Good vs Bad loans
SELECT loan_status, COUNT(*) 
FROM loans
GROUP BY loan_status;

-- Avg interest rate by grade
SELECT grade, AVG(int_rate)
FROM loans
GROUP BY grade;

-- Default rate by purpose
SELECT purpose,
       SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END)*100.0/COUNT(*) AS default_rate
FROM loans
GROUP BY purpose;




