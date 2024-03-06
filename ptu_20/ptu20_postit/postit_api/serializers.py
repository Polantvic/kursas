from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user_id')
    user_username = serializers.ReadOnlyField(source='user.username')
    post = serializers.ReadOnlyField(source='post_id')

    class Meta:
        model = models.Comment
        fields = ['id', 'body', 'post', 'created_at', 'updated_at',
                  'user', 'user_username']


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user_id')
    user_username = serializers.ReadOnlyField(source='user.username')
    comments = CommentSerializer(many=True, read_only=True)
#    comments = serializers.StringRelatedField(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()

    def get_comment_count(self, obj):
        return models.Comment.objects.filter(post=obj).count()

    class Meta:
        model = models.Post
        fields = ['id', 'title', 'body', 'created_at', 'updated_at',
                  'user', 'user_username', 'comment_count', 'comments']
