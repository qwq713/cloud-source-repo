import boto3

"""
구현 로직

1.대상 정보 수집
    - ELB 정보 수집 ( describe-load-balancers ) / By *
        - LoadBalancerArn , LoadBalancerName , Type
    - ELB Listener 정보 수집 ( describe-listeners ) / By LoadBalancerArn ( PK : )
        - ListenerArn , LoadBalancerArn , TargetGroupArn , Protocol, Port
    - ELB TargetGroup 정보 수집 ( describe-target-groups ) / By *
        - TargetGroupArn, Protocol, Port , LoadBalancerArns
    - ELB TargetGroup 정보 수집 2 ( describe-target-health ) / By TargetGroupArn
        - Target.Id , Target.Port

2.연결 정보 파악
    - ELB & TargetGroup
        -  TargetGroupArn -> LoadBalancerArn
    - TargetGroup & EC2
        - TargetGroupArn -> Target

3.태깅 대상 선정
    - ELB : LoadBalancerName
    - TargetGroup : LoadBalancerName -  Listener Protocol & port - TargetGroup Protocol & TargetPort
    - EC2 : LoadBalancerName

"""