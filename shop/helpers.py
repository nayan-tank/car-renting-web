from django.core.exceptions import ValidationError

# clean city name
def clean_city_name(value):
    if not value.isalpha():
        raise ValidationError('city name must be string')


# clean area pincode
def clean_area_pincode(value):
    if not value.isnumeric():
        raise ValidationError('area pincode must be number')

# clean area name
def clean_area_name(value):
    if value.isnumeric():
        raise ValidationError('area name should not be number')


# clean brand name
def clean_brand_name(value):
    if not value.isalpha():
        raise ValidationError('brand name must be string')

# clean contact
def clean_contact(value):
    if not value.isnumeric():
        raise ValidationError('contact name must be number')

# clean color
def clean_color(value):
    if not value.isalpha():
        raise ValidationError('color name must be string')

# clean registration no
def clean_regno(value):
    if value.isnumeric() or value.isalpha():
        raise ValidationError('registration no must be alpha numeric')

# clean car name
def clean_car_name(value):
     if value.isnumeric():
        raise ValidationError('car name must be numeric')

# clean fuel type
def clean_fuel_type(value):
    if not value.isalpha():
        raise ValidationError('fuel type must be string')

# clean model name
def clean_model_name(value):
    if value.isnumeric():
        raise ValidationError('model name can not be numeric')

# clean transmission
def clean_transmission(value):
    if not value.isalpha():
        raise ValidationError('transmission name must be string')

# clean transmission
def clean_car_parts(value):
    if value.isnumeric():
        raise ValidationError('car parts can not be numeric')

# clean inquiry text
def clean_inq_text(value):
    if value.isnumeric():
        raise ValidationError('Enter a valid inquiry text !!')  

# clean complain subject
def clean_complain_sub(value):
    if value.isnumeric():
        raise ValidationError('Enter a valid subject text !!')

# clean complain text
def clean_complain_text(value):
    if value.isnumeric():
        raise ValidationError('Enter a valid complain text !!')

# clean feedback text
def clean_review_text(value):
    if value.isnumeric():
        raise ValidationError('Enter a valid review text !!')