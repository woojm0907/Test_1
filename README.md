# Test_1

이게 이제 되네 
 
 # 해당 파일은 작성자의 임의적 테스트 파일입니다.
 
 - 실험 중이므로 조심해야 합니다.

 ## 레포지토리 복제 깃허브 상단 URL 붙이기


```bash
git commit -m "a"

git push

git add . (내 경로 기준으로 하위폴더 싹다 저장/상대 경로)
```

### 절대경로: 시작(EX: C드라이브)맨처음부터 그아래의 전체적 경로 및 하위폴더까지의 경로. 고정경로, 

```bash
Docker 버전 확인: docker --version
Docker 상세 정보: docker info (설치 상태 확인용)
Git 버전 확인: git --version
OS 정보: (Windows라면 systeminfo, Mac이라면 sw_vers)
```

### 프로젝트 개요(미션 목표 요약)






### 실행 환경(OS/쉘/터미널, Docker 버전, Git 버전)

```bash
Microsoft Windows 11 Pro

Name                           Value                                 
----                           -----                                 
PSVersion                      5.1.26100.8875                        
PSEdition                      Desktop                               
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0...}               
BuildVersion                   10.0.26100.8875                       
CLRVersion                     4.0.30319.42000                       
WSManStackVersion              3.0                                   
PSRemotingProtocolVersion      2.3                                   
SerializationVersion           1.1.0.1   

Docker version 29.6.2, build dfc4efb

git version 2.55.0.windows.3
```

### 수행 항목 체크리스트(터미널/권한/Docker/Dockerfile/포트/볼륨/Git/GitHub)

터미널


파일권한
total 0
-rw-r--r--    1 root     root             0 Aug  5 05:12 Dockerfile
drwxrwxrwx    1 root     root          4096 Jul 31 07:20 Test_1

도커 목록
Usage:  docker image COMMAND

Manage images

Commands:
  build       Build an image from a Dockerfile
  history     Show the history of an image
  import      Import the contents from a tarball to create a filesystem image
  inspect     Display detailed information on one or more images
  load        Load an image from a tar archive or STDIN
  ls          List images
  prune       Remove unused images
  pull        Download an image from a registry
  push        Upload an image to a registry
  rm          Remove one or more images
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE

Run 'docker image COMMAND --help' for more information on a command.


 i Info →   U  In Use
IMAGE   ID             DISK USAGE

CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS  gi   NAMES

DRIVER    VOLUME NAME



### 검증 방법(어떤 명령으로 무엇을 확인했는지) + 결과 위치 링크






### 트러블슈팅 2건 이상(문제 → 원인 가설 → 확인 → 해결/대안)

#### 1. 

```bash
DESKTOP-IM37LLL:/mnt/host/c/Users/USER/Desktop/test_1/Test_1# echo "OS: $(cat /etc/issue | head -n 1)"
OS: This is Docker Desktop's WSL 2 LinuxKit bootstrap environment, intended for debugging only
DESKTOP-IM37LLL:/mnt/host/c/Users/USER/Desktop/test_1/Test_1# echo "Shell: $SHELL"
Shell: /bin/sh
DESKTOP-IM37LLL:/mnt/host/c/Users/USER/Desktop/test_1/Test_1# git --version
git version 2.52.0
DESKTOP-IM37LLL:/mnt/host/c/Users/USER/Desktop/test_1/Test_1# docker --version

It looks like you have tried to invoke the docker CLI from the docker-desktop WSL2 distribution. This is not supported.

Please invoke the docker CLI from the Windows Command Prompt, PowerShell, or other compatible terminals.

If you wish to interact with Docker Desktop from a third-party WSL2 distribution, such as Ubuntu, please enable the Docker Desktop WSL2 integration for it. See: https://docs.docker.com/desktop/wsl/#enabling-docker-support-in-wsl-2-distrosDESKTOP-IM37LLL:/mnt/host/c/Users/USER/Desktop/test_1/Test_1# 
```
문제 이유 : 작업기기의 경우 윈도우 체제를 사용하며 윈도우 언어인 파워쉘(PowerShell)이 기본으로 되어있습니다. 그로 인해서 ios에서 사용되는 리눅스 언어인 wsl 언어에서는서로 구동을 제대로 할수 없어서 정보를 가져올 수 없는 것이 이유였습니다. 즉 다른 체제 사이의 연결 문제라는 점이었습니다.

 즉 Docker Desktop이 설치된 윈도우와 현재 사용 중인 WSL(리눅스 환경)이 서로 연결되어 있지 않기 때문입니다. 

그래서 Docker Desktop에서 Resources -> WSL Integration를 켜주었는데도 안되서 보니 도커 전용 관리 구역이라서 명령어를 쳐도 작동을 안했던 것이었습니다.

해결방법 : 결국 파워쉘(PowerShell)로 바꾸어서 명령어를 입력하여 작동시키니 정상적으로 작동했습니다.

....

##### 기술 문서만 읽어도 전체 수행 내용을 파악할 수 있어야 한다.

---------------------------------------------------------------