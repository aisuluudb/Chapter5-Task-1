# select first_name "First Name", last_name "Last Name" from employees;
# select department_id from employees;
# select * from employees order by first_name DESC;
# select employee_id, first_name, last_name, salary from employees order by salary;
# select count(*) from employees;
# select first_name, last_name, salary from employees where salary NOT BETWEEN 10000 and 15000;
# select first_name, last_name, department_id from employees where department_id in (30,100) order by department_id ASC;
# select first_name, last_name, hire_date from employees where year(hire_date) like '1987';
# select last_name, job_id, salary from employees where job_id in ('it_prog','sh_clerk') 
# and salary not in (4500, 10000, 15000);
# select * from employees where last_name in ('BLAKE', 'SCOTT', 'KING', 'FORD');
# select sum(salary) from employees;
# select min(salary) from employees;
# select AVG(salary), count(*) from employees where department_id = 90;
# select job_id, count(*) from employees group by job_id;
# select job_id, AVG(salary)  from employees where job_id <> 'IT_PROG' group by job_id;

--joins--
# select location_id, street_address, city, state_province, country_name from locations natural join countries;
# select first_name, last_name, department_id, department_name from employees join departments using (department_id);
# SELECT e.employee_id 'Emp_Id', e.last_name 'Employee', 
#     -> m.employee_id 'Mgr_Id', m.last_name 'Manager' 
#     -> FROM employees e 
#     -> join employees m 
#     -> ON (e.manager_id = m.employee_id);
# SELECT d.department_name, e.first_name, l.city 
# FROM departments d 
# JOIN employees e 
# ON (d.manager_id = e.employee_id) 
# JOIN locations l USING (location_id);

# ???Write a query to display department name, name (first_name, last_name), 
# hire date, salary of the manager for all managers whose experience is more than 15 years
# SELECT first_name, last_name, hire_date, salary, 
# (DATEDIFF(now(), hire_date))/365 Experience 
# FROM departments d JOIN employees e 
# ON (d.manager_id = e.employee_id) 
# WHERE (DATEDIFF(now(), hire_date))/365>15;

# --datetime--

#
# SELECT MAKEDATE(EXTRACT(YEAR FROM CURDATE()),1)
# SELECT DATE_FORMAT(CURDATE(),'%M %e, %Y') 
#    AS 'Current_date';
# select first_name, last_name from employees where month (hire_date) = 6;
# SELECT FIRST_NAME, SYSDATE(), HIRE_DATE, DATEDIFF( SYSDATE(), hire_date )/365
#   FROM employees;






