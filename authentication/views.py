from rest_framework import generics,permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model,authenticate
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.exceptions import NotFound
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth.models import User

User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate JWT Tokens
            refresh = RefreshToken.for_user(user)

            # Prepare user response data
            user_data = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "phone": user.phone,  # ✅ Include phone
                "address": user.address,  # ✅ Include address
                "role": "admin" if user.is_staff else "standard"
            }

            return Response({
                "message": "User registered successfully",
                "user": user_data,
                "tokens": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login User
class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get("username")  # Change to "email" if needed
        password = request.data.get("password")

        try:
            # Check if user exists before authenticating
            user = User.objects.filter(username=username).first()
            if not user:
                return Response({"message": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)
            
            # Authenticate the user
            user = authenticate(username=username, password=password)
            if not user:
                return Response({"message": "Invalid password."}, status=status.HTTP_401_UNAUTHORIZED)

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)

            # Prepare user data for response
            user_data = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "phone": getattr(user, "phone", None),  # If phone exists
                "address": getattr(user, "address", None),  # If address exists
                "role": "admin" if user.is_staff or user.is_superuser else "standard"
            }

            return Response({
                "message": "Login successful",
                "user": user_data,
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# List All Users
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# Retrieve a Single User
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# Update User
class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# Delete User
class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        """Override get_object to handle user not found error."""
        try:
            return super().get_object()
        except User.DoesNotExist:
            raise NotFound({"message": "User does not exist"})

    def destroy(self, request, *args, **kwargs):
        """Override destroy to return success message after deletion."""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)
