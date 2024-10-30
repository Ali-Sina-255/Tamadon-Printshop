from rest_framework import serializers

from .models import Category, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]  # Include necessary fields


class OrderSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all()
    )

    class Meta:
        model = Order
        fields = ["id", "user", "description", "category", "created_at", "updated_at"]

    def create(self, validated_data):
        categories_data = validated_data.pop("category")
        order = Order.objects.create(**validated_data)

        # Add categories to the order
        order.category.set(categories_data)  # Use set() to associate categories
        return order

    def update(self, instance, validated_data):
        categories_data = validated_data.pop("category", None)

        # Update order fields
        instance.user = validated_data.get("user", instance.user)
        instance.description = validated_data.get("description", instance.description)
        instance.save()

        # Update categories if provided
        if categories_data is not None:
            instance.category.set(categories_data)  # Use set() to update categories

        return instance
