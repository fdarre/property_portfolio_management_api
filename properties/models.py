from address.models import AddressField
from django.db import models


class Building(models.Model):
    address = AddressField()
    number_of_units = models.IntegerField(max_length=20, null=True, blank=True)
    number_of_floors = models.IntegerField(max_length=20)
    surface_area = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    ownerName = models.CharField(max_length=30, null=True, blank=True)
    construction_date = models.DateField(null=True, blank=True)
    acquisition_date = models.DateField(null=True, blank=True)
    acquisition_price = models.DecimalField(
        max_digits=9, decimal_places=2, null=True, blank=True
    )
    current_price = models.DecimalField(
        max_digits=9, decimal_places=2, null=True, blank=True
    )
    is_co_ownership = models.BooleanField()

    is_in_protected_heritage_area = models.BooleanField()

    def __str__(self):
        return f"{self.address}"


class Unit(models.Model):
    class Positions(models.TextChoices):
        LEFT = "le", "Left"
        RIGHT = "ri", "Right"
        CENTRE = "ce", "Center"
        CENTRE_LEFT = "cl", "Center Left"
        CENTRE_RIGHT = "cr", "Center Right"

    class Properties_type(models.TextChoices):
        APPARTMENT = "ap", "Appartment"
        HOUSE = "ho", "House"

    property_type = models.CharField(max_length=2, choices=Properties_type.choices)
    floor = models.IntegerField(null=True, blank=True)
    position = models.CharField(
        max_length=2, choices=Positions.choices, null=True, blank=True
    )
    surface_area = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    #@todo: add uploadable picture
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.building}, floor: {self.floor}, posistion: {self.position}"


class Expense(models.Model):
    class Categories(models.TextChoices):
        TAXES = "ta", "Taxes"
        WATER_BILL = "wb", "Water Bill"
        ELECTRICITY_BILL = "eb", "Electricity Bill"
        INSURANCE_COTISATION = "ic", "Insurance Cotisation"
        ACCOUNTANT_FEES = "af", "Accountant Fees"
        REALTOR_FEES = "rf", "Realtor Fees"
        DIAGNOSTICIAN_FEES = "df", "Diagnostician Fees"
        LEGAL_FEES = "lf", "Legal Fees"
        CONDO_FEES = "cf", "Condo Fees"
        OVERPAYMENT_REFUND = "or", "Overpayment Refund"

    category = models.CharField(max_length=2, choices=Categories.choices)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    observations = models.CharField(max_length=100, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category}, {self.amount}" #@todo: Display the chosen currency


class Income(models.Model):
    class Categories(models.TextChoices):
        INSURANCE_COMPENSATION = "ic", "Insurance Compensation"
        RENT = "re", "Rent"
        HOUSING_ALLOWANCE = "ha", "Housing Allowance"
        OTHER_PAYMENT = "ot", "Other Payment"

    category = models.CharField(max_length=2, choices=Categories.choices)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    observations = models.CharField(max_length=100, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category}, {self.amount}" #@todo: Display the chosen currency
