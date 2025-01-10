import psycopg2

# database connectivity

DB_CONFIG = {
    "dbname":"employee",
    "user":"postgres",
    "password":"password",
    "host":"localhost",
    "port":5432

}

def connect_db():
     """Connect to the postgreSQL database"""
     try:
        conn=psycopg2.connect(**DB_CONFIG)
        print("Connection Succesful to database")
        return conn
     except Exception as e:
        print("Error connecting to database",e)
        return None
#connect_db()


def add_employee(name,position,salary):
   query="INSERT INTO employees (name,position,salary) VALUES(%s,%s,%s)"
   conn=connect_db()
   if conn:
      try:
         with conn.cursor() as cursor:
            cursor.execute(query,(name,position,salary))
            conn.commit()
            print("Employee added successfully...")
      except Exception as e:
         print("Error adding employee",e)
      finally:
         conn.close()
#add_employee('ABCD','HR',30000)


def view_employees():
   query="SELECT * FROM employees "
   conn=connect_db()
   if conn:
      try:
         with conn.cursor() as cursor:
            cursor.execute(query)
            employees=cursor.fetchall()
            print("\n Employee List:")
            for emp in employees:
               print(f"Id:{emp[0]},Name:{emp[1]},Position:{emp[2]},Salary:{emp[3]}")
      except Exception as e:
         print("Error retriving employees",e)
      finally:
         conn.close()
#view_employees()

def update_employees(empid,name=None,position=None,salary=None):
   query="UPDATE employees SET name=COALESCE(%s,name),position=COALESCE(%s,position),salary=COALESCE(%s,salary) WHERE id=%s"
   conn=connect_db()
   if conn:
      try:
         with conn.cursor() as cursor:
            cursor.execute(query,(name,position,salary,empid))
            conn.commit()
            print("Employee updated successfully")
      except Exception as e:
         print("Error updating employee",e)
      finally:
         conn.close()
#update_employees(2,"Mohit","Prof",999999)



def delete_employee(empid):
   query="DELETE FROM employees where id=%s"
   conn=connect_db()
   if conn:
      try:
          with conn.cursor() as cursor:
            cursor.execute(query,(empid,))
            conn.commit()
            print("Employee Details Deleted")
      except Exception as e:
            print("Error Deleting Details",e)
      finally:
            conn.close()
#delete_employee(2)


def main():
   '''Main menu for EMS'''
   while True:
      print("\nEMPLOEE MANAGEMENT SYSTEM")
      print("1.Add Employee")
      print("2. View Employess")
      print("3.Update Employee")
      print("4. Delet Employee")
      print("5.Exit")

      choice=input("enter your choice:")
      if choice=="1":
         name=input("Enter Employee Name")
         position=input("Enter Employee Position")
         salary=int("Enter salary")
         add_employee(name,position,salary)

      elif choice=="2":
         view_employees()


      elif choice=="3" :
         empid=int(input("Enter Employee ID:"))
         name=input("Enter new Name:") or None
         position=input("Enter Position") or None
         salary=input("Enter Salary:")
         salary=int(salary) if salary else None
         update_employees(empid,name,position,salary)

      elif choice=="4":
         empid=int(input("Enter Employee Id to delete:"))
         delete_employee(empid)
            
      elif choice=="5":
         print("System Exited")
         break
      else:
         print("Invalid choice try again..")

if __name__ =="__main__":
   main()




