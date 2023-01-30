from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Post, Group, User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(read_only=True,
                              slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post', )


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(read_only=True, slug_field='username',
                            default=serializers.CurrentUserDefault())

    following = SlugRelatedField(queryset=User.objects.all(),
                                 slug_field='username')

    class Meta:
        fields = '__all__'
        model = Follow

        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate_following(self, following_user):
        if following_user == self.context['request'].user:
            raise serializers.ValidationError('Нельзя подписаться '
                                              'на самого себя')

        return following_user
