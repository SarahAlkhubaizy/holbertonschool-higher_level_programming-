-- creates the user user_0d_1 if it does not already existCREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
-- give grants to user-- grants all privileges on all databases to user_0d_1
GRANT ALL PRIVILEGES 
ON *.*
TO 'user_0d_1'@'localhost';
