from datetime import  datetime

suppliers = [
  {
    'id': '8bf4ac2e-4eef-4e50-95d6-fdbc9ae1194f',
    'name': 'Milk Supplier',
    'address': '77 Milk Way',
    'contactNumber': '0987654321',
    'email': 'milk@milksupplier.com'
  },
]

ingredients = [
  {
    'id': '602f2ab3-97bd-468e-a88b-bb9e00531fd0',
    'name': 'Milk',
    'stock': {
      'quantity': 100.0,
      'unit': 'LITERS',
    },
    'products': [],
    'supplier': '8bf4ac2e-4eef-4e50-95d6-fdbc9ae1194f',
    'lastUpdated': datetime.utcnow(),
  }
]

products = [
  {
    'id': '6f97f960-3471-4157-b823-776e7a74ca29',
    'name': 'Walnut Bomb',
    'price': 37.0,
    'size': 'MEDIUM',
    'available': False,
    'ingredients': [
      {
        'ingredient': '602f2ab3-97bd-468e-a88b-bb9e00531fd0',
        'quantity': 100.0,
        'unit': 'LITERS',
      }
    ],
    'hasFilling': False,
    'hasNutsToppingOption': True,
    'lastUpdated': datetime.utcnow(),
  },
  {
    'id': 'a53e4146-7429-460c-b2f4-c2114574c8b0',
    'name': 'Cappuccino Star',
    'price': 12.50,
    'size': 'SMALL',
    'available': True,
    'ingredients': [
      {
        'ingredient': '602f2ab3-97bd-468e-a88b-bb9e00531fd0',
        'quantity': 100.0,
        'unit': 'LITERS',
      }
    ],
    'hasCreamOnTopOption': True,
    'hasServeOnIceOption': True,
    'lastUpdated': datetime.utcnow(),
  },
]
