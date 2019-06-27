from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):

	class Meta:
		model = Stock
		#fields = ('ticker', 'volume') To return only specific vales to users
		fields = '__all__' #to return all values to user try 
		
