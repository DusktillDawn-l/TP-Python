#9-6冰淇凌小店
class Restaurant():
	'''模拟餐厅'''
	
	def __init__(self,restaurant_name,cuisine_type):
		'''初始化属性餐厅名和烹饪方式'''
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.number_served=0
		
	def describe_restaurant(self):
		'''告知餐厅的各项信息'''
		print(self.restaurant_name.title())
		print(self.cuisine_type.title())
	
	def open_restaurant(self):
		'''告知餐厅在正常开张'''
		print(self.restaurant_name.title()+' is opening')
		
	def set_number_served(self,number_served):
		'''设置就餐人数'''
		self.number_served=number_served
		
	def increment_number_served(self,additional_served):
		'''增加就餐的人数'''
		self.number_served +=additional_served
		
class IceCreamStand(Restaurant):
	'''模拟冰淇凌站'''
	
	def __init__(self,name,cuisine_type='ice_cream'):
		'''初始化冰淇凌站的属性'''
		super().__init__(name, cuisine_type)
		self.flavors = []
		
	def show_flavors(self):
		"""Display the flavors available."""
		print("\nWe have the following flavors available:")
		for flavor in self.flavors:
			print("- " + flavor.title())

big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()
		
#9-7管理员
class User():
	'''模拟用户'''
	
	def __init__(self,first_name,last_name):
		'''初始化客户的姓和名'''
		self.first_name=first_name
		self.last_name=last_name
		self.login_attempts=0
	
	def describe_user(self):
		'''打印用户信息摘要'''
		print(self.first_name+self.last_name)
		
	def greet_user(self):
		'''向用户问好'''
		print("Hello, "+self.first_name+self.last_name)
		
	def increment_login_attempts(self):
		'''将属性login_attempts的值加一'''
		self.login_attempts+=1
		
	def reset_login_attempts(self):
		self.login_attempts=0

class Admin(User):
	'''初始化用户'''
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.privileges=[]
		
	def show_privileges(self):
		for privilege in self.privileges:
			print('you can '+privilege)
		
leon=Admin('恒','孙')
leon.describe_user()
leon.privileges=['can reset passwords',
    'can moderate discussions',
    'can suspend accounts']
    
leon.show_privileges()

#9.8权限
class User():
	'''模拟用户'''
	
	def __init__(self,first_name,last_name):
		'''初始化客户的姓和名'''
		self.first_name=first_name
		self.last_name=last_name
		self.login_attempts=0
	
	def describe_user(self):
		'''打印用户信息摘要'''
		print(self.first_name+self.last_name)
		
	def greet_user(self):
		'''向用户问好'''
		print("Hello, "+self.first_name+self.last_name)
		
	def increment_login_attempts(self):
		'''将属性login_attempts的值加一'''
		self.login_attempts+=1
		
	def reset_login_attempts(self):
		self.login_attempts=0

class Admin(User):
	'''初始化用户'''
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.privileges=Privileges()
		
	def show_privileges(self):
		for privilege in self.privileges:
			print('you can '+privilege)
class Privileges():
	'''模拟特权'''
	
	def __init__(self,privileges=[]):
		'''初始化特权'''
		self.privileges=privileges
    
	def show_privileges(self):
		if self.privileges:
			for privilege in self.privileges:
				print('you can '+privilege)
				
	
eric = Admin('eric', 'matthes')
eric.describe_user()

eric.privileges.show_privileges()

print("\nAdding privileges...")
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()

#9-9电瓶升级
class Car():
	'''一次模拟汽车的简单尝试'''
	def __init__(self,make,model,year):
		'''初始化描述汽车的属性'''
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	
	def get_descriptive_name(self):
		'''返回整洁的描述性信息'''
		long_name = str(self.year)+' ' +self.make+' '+self.model
		return long_name.title()
		
	def read_odometer(self):
		'''打印一条指出汽车总里程的消息'''
		print('This car has ' + str(self.odometer_reading) + " miles on it.")
		
	def update_odometer(self,mileage):
		'''
		将里程数设置为设定的值
		禁止里程往回调
		'''
		if mileage >=self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print("You can't roll back an odometer!")
			
	def increment_odometer(self,miles):
		'''将里程表读书增加指定的量'''
		self.odometer_reading += miles

class Battery():
	'''一次模拟电动汽车电瓶的简单尝试'''
	
	def __init__(self,battery_size=70):
		'''初始化电瓶信息'''
		self.battery_size = battery_size
	def describe_battery(self):
		'''打印一条描述电瓶容量的消息'''
		print("This car has a "+str(self.battery_size)+"-KWH batery.")
		
	def get_range(self):
		'''打印一条信息，指出电瓶的续航里程'''
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
		
	def upgrade_battery(self):
		'''升级电池如果电量不足85，则调整到85'''
		if self.battery_size !=85:
			self.battery_size =85		 
			print('Your battery size has been upgraded to 85-kwh')
		else:
			print("Your battery has already been upgraded to 85-kwh, \
you don't need upgrade.")

class ElectricCar(Car):
	'''电动汽车的独特之处'''
	
	def __init__(self,make,model,year):
		'''
		电动汽车的独特之处
		初始化父类的属性，再初始化电动汽车特有的属性
		'''
		super().__init__(make,model,year)
		self.battery = Battery()
			
	def fill_gas_tank(self):
		'''电动车没有油箱'''
		print("This car doesn't need a gas tank!")
		

			
new_car=ElectricCar('YiQi','Audi',2020)
new_car.battery.get_range()
new_car.battery.upgrade_battery()
new_car.battery.upgrade_battery()
