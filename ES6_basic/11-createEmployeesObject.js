export default function createEmployeesObject(departmentName, employees) {
    const Employees_Object = {
        [departmentName]: employees
    };

    return Employees_Object;
}