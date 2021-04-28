from rest_framework import viewsets
from rest_framework import permissions
from arctictest.serializers import CandidateSerializer, ScoreSerializer
from arctictest.models import Candidate,Score

class createcandidates(viewsets.ModelViewSet):
    """
    API endpoint that allows candidates to be created.
    """
    serializer_class = CandidateSerializer
    permission_classes = [permissions.IsAuthenticated]
    try:
        queryset = Candidate.objects.save()
    except:
        exit(1)



class getcandidates(viewsets.ModelViewSet):
    """
    API endpoint that allows candidates to be viewed.
    """
    serializer_class = CandidateSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Candidate.objects.all().order_by('name')