class StructureValidations:
    def __init__(self, requirements):
        self.requirements = requirements
        self.valid_types = ['LEN', 'LETTERS', 'SPECIALS', 'NUMBERS']
        self.valid_conditions = ['<', '>', '=']
        
    def validate_empty_list(self):
        if len(self.requirements) == 0:
            raise ValueError('The requirement list should contain at least one tuple with three conditions.')
          
    def validate_tuple(self):
        for req in self.requirements:
            if len(req) != 3:
                 raise ValueError('The tuple must contain three values.')

    def validate_types(self): 
        for req in self.requirements:    
            if req[0] not in self.valid_types:
                raise ValueError("The requirement type isn't valid. The valid values are 'LEN', 'LETTERS', 'SPECIALS' or 'NUMBERS' and they must be in uppercase.")
    
    def validate_conditions(self):
        for req in self.requirements:
            if req[1] not in self.valid_conditions:
                raise ValueError("The condition type isn't valid. The valid values are '<', '>' or '='.")
                
    def validate_num(self):
        for req in self.requirements:
            if not isinstance(req[2], int):   
                raise ValueError("The condition number isn't valid. It must be an integer.")  
 
def num_letters(value):
    count = 0
    for letter in value:
        if letter.isalpha():    
            count +=1
    return count

def num_numbers(value):
    count = 0
    for letter in value:
        if letter.isdigit():    
            count +=1
    return count
    
def num_specials(value):
    count = 0
    for letter in value:
        if not letter.isalnum():    
            count +=1
    return count
    
def condition_satisfied(value, condition, req_num):
    if condition == '<':
        return True if value < req_num else False
    if condition == '>':
        return True if value > req_num else False
    if condition == '=':
        return True if value == req_num else False
    
def validate_requirements(requirements, password):
    validation = StructureValidations(requirements)
    validation.validate_empty_list()
    validation.validate_tuple()
    validation.validate_types()
    validation.validate_conditions()
    validation.validate_num()
        
    for req in requirements:
        req_type = req[0]
        req_condition = req[1]
        req_num = req[2]
        
        if req_type == 'LEN':
            if not condition_satisfied(len(password), req_condition, req_num):
                return False     
        if req_type == 'LETTERS':
            if not condition_satisfied(num_letters(password), req_condition, req_num):
                return False
        if req_type == 'NUMBERS':
            if not condition_satisfied(num_numbers(password), req_condition, req_num):
                return False
        if req_type == 'SPECIALS':
            if not condition_satisfied(num_specials(password), req_condition, req_num):
                return False       
    return True    

def test_passwords():
    assert validate_requirements([('SPECIALS', '=', 1), ('NUMBERS', '<', 10), ('LETTERS', '=', 0), ('LEN', '>', 8)], '@12345678') == True
    assert validate_requirements([('SPECIALS', '>', 1)], '@123') == False
    assert validate_requirements([('LETTERS', '<', 1)], '@12399%%%') == True
    assert validate_requirements([('NUMBERS', '=', 1)], 'fdfgre22') == False
    assert validate_requirements([
                                 ('SPECIALS', '>', 0),
                                 ('LETTERS', '<', 10),
                                 ('NUMBERS', '=', 5),
                                 ('SPECIALS', '<', 4),
                                 ('LETTERS', '>', 1),
                                 ('LEN', '>', 10),
                                 ('LEN', '<', 15),
                                 ('SPECIALS', '=', 2),
                                 ], '12345@!ABCD') == True
    assert validate_requirements([('NUMBERS', '=', 1), ('LETTERS', '=', 1)], '@@12AA') == False

test_passwords()
print('='*20)
print('All tests passed!')
print('='*20)
print()
print("Now I'll show invalid structure errors: \n")

try:
    validate_requirements([('=', 'a')], '123456') 
except Exception as e:
    print("([('=', 'a')], '123456') ->", e)

try:
    validate_requirements([('LETTERS', '=', 'a')], '123456')
except Exception as e:
    print("([('LETTERS', '=', 'a')], '123456') ->", e)    
    
try:
    validate_requirements([], '123456')
except Exception as e:
    print("([], '123456') ->", e)
    
try:
    validate_requirements([('SPECIALS', 'X', 1)], '123456')
except Exception as e:
    print("([('SPECIALS', 'X', 1)], '123456') ->", e)
    
print("\nThe error messages above were supressed by the try/except block.")
print('='*20)
print()
print("Now I will force the error to raise and finish the script: \nExample: ([('NUMBEEEERS', '=', '1')], '123456')\n")
validate_requirements([('NUMBEEEERS', '=', '1')], '123456')