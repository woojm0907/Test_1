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
DESKTOP-IM37LLL:/mnt/host/c/Users/USER/Desktop/test_1/Test_1# cat /etc/os-release
PRETTY_NAME="Docker Desktop"
DESKTOP-IM37LLL:/mnt/host/c/Users/USER/Desktop/test_1/Test_1# echo $SHELL
/bin/sh
DESKTOP-IM37LLL:/mnt/host/c/Users/USER/Desktop/test_1/Test_1# docker --version

It looks like you have tried to invoke the docker CLI from the docker-desktop WSL2 distribution. This is not supported.

Please invoke the docker CLI from the Windows Command Prompt, PowerShell, or other compatible terminals.

If you wish to interact with Docker Desktop from a third-party WSL2 distribution, such as Ubuntu, please enable the Docker Desktop WSL2 integration for it. See: https://docs.docker.com/desktop/wsl/#enabling-docker-support-in-wsl-2-distrosDESKTOP-IM37LLL:/mnt/host/c/Users/USER/Desktop/test_1/Test_1# git --version
git version 2.52.0
```

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

### 수행 항목 체크리스트(터미널/권한/Docker/Dockerfile/포트/볼륨/Git/GitHub)






### 검증 방법(어떤 명령으로 무엇을 확인했는지) + 결과 위치 링크






### 트러블슈팅 2건 이상(문제 → 원인 가설 → 확인 → 해결/대안)






##### 기술 문서만 읽어도 전체 수행 내용을 파악할 수 있어야 한다.

---------------------------------------------------------------