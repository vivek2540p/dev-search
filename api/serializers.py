from rest_framework import serializers
from projects.models import Project,Tag,Review
from users.models import Profiles

class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
        
class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

class ProjectSerializer(serializers.ModelSerializer):
    owner=ProfilesSerializer(many=False)
    tags=TagSerializer(many=True)
    reviews=serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = '__all__'
        # fields = ('id', 'title', 'description', 'image')
    
    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data
    
    
