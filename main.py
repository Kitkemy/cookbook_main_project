import requests
import json
import pprint

#jak najlepiej pobrac skladniki i zintegrować je z ilościami??? do slownika?

class Meal:
    def __init__(self, meal_selection):
        self.meal_selection = meal_selection
        self.data = self.get_data()
        self.name = self.get_name()
        self.img_path = self.get_img_path()
        self.instruction = self.get_instruction()
        self.ingredients = self.get_ingredients()
        
    def get_random_data(self):
            r = requests.get('http://www.themealdb.com/api/json/v1/1/random.php')
            response = r.json()
            #pprint.pprint(response)
            return response

    def get_data(self):
        if self.meal_selection == "random":
            response = self.get_random_data()
        elif self.meal_selection == "category":
            pass
            #metoda dla category i dalej kolejna po głównym składniku
        return response
    
    def get_name(self):
        name = self.data['meals'][0]['strMeal']
        return name

    def get_img_path(self):
        img_path = self.data['meals'][0]['strMealThumb']
        return img_path

    def get_instruction(self):
        instruction = self.data['meals'][0]['strInstructions']
        return instruction

    def get_ingredients(self):
        ingredients = {}
        for i in range(20): 
            i = i + 1
            ingredients[(self.data['meals'][0]['strIngredient'+str(i)])] = [(self.data['meals'][0]['strMeasure'+str(i)])]
        return ingredients



meal = Meal("random")
print(meal.name)
print('\n')
print(meal.img_path)
print('\n')
print(meal.instruction)
print('\n')
print(meal.ingredients)


#yutube i category add, area
#dodac kategorie
#dodac szukanie po kategoriach
#szukanie po głownym skladniku
#zaczac  flaska- zeby dane wpisane recznie wyswietlily sie na stronie