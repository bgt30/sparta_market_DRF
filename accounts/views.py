from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework import status

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

class LoginView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
        )
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'token': str(refresh.access_token),
            })
        return Response({'error': '로그인 실패'}, status=400)

class ProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'username' 

class LogoutView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "로그아웃 성공"})
        except Exception:
            return Response({"message": "로그아웃 실패"}, status=400)

class ProfileUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'username'

    def get_object(self):
        return self.request.user

class PasswordChangeView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PasswordChangeSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        user = request.user
        if not user.check_password(request.data.get('old_password')):
            return Response({"error": "현재 비밀번호가 일치하지 않습니다."}, 
                          status=status.HTTP_400_BAD_REQUEST)
        # 비밀번호 복잡성 검증 추가 필요

class AccountDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request):
        user = request.user
        if user.check_password(request.data.get('password')):
            user.delete()
            return Response({"message": "계정이 삭제되었습니다."})
        return Response({"error": "비밀번호가 일치하지 않습니다."}, status=400)

class FollowView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, username):
        user_to_follow = get_object_or_404(User, username=username)
        if request.user == user_to_follow:
            return Response({"error": "자기 자신을 팔로우할 수 없습니다."}, status=400)
        
        if request.user in user_to_follow.followers.all():
            user_to_follow.followers.remove(request.user)
            return Response({"message": "언팔로우 완료"})
        else:
            user_to_follow.followers.add(request.user)
            return Response({"message": "팔로우 완료"}) 