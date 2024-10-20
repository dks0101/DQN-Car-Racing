# DQN-Car-Racing Project

이 프로젝트는 DQN 알고리즘을 사용하여 `CarRacing-v2` 환경에서 자동차를 주행하는 agent를 학습시키고, 그 성과를 평가합니다.

## 프로젝트 파일 구조

### 학습에 필요한 파일들

- **requirements.txt**: DQN 학습을 위해 필요한 라이브러리와 그 버전 정보를 담고 있습니다. 다음 명령어로 필요한 라이브러리들을 설치할 수 있습니다.
  ```bash
  pip install -r requirements.txt

- **__init__.py**: 모듈을 초기화하는 역할을 하며, `utils.py`에 있는 함수와 클래스를 가져옵니다.

## 학습 코드

- **DQN-CarRacing.ipynb**:  
  Q-learning을 `MiniGrid-Empty` 환경에서 학습시킨 코드입니다.
  
## src 폴더

- **CNN.py**:  
  DQN에서 상태 공간을 처리하기 위한 CNN 모델 정의 & 입력 이미지를 통해 각 action의 value 출력합니다.
  그리고 CNN의 kernel size와 stride를 바꿔주었습니다.
  
- **DQN.py**:  
  DQN을 구현한 클래스와 경험 리플레이를 위한 버퍼를 정의 & CNN을 사용하여 상태를 입력받아 각 행동의 가치를 추정하고 학습합니다.

- **Preprocess.py**:  
  CarRacing-v2 환경의 이미지 프레임을 전처리하여 특정 영역을 자르고 그레이스케일로 변환한 후 정규화하여 CNN 입력 형식에 맞게 변환하는 클래스 정의합니다.

- **evaluate.py**:  
  CarRacing-v2 환경에서 DQN 에이전트를 평가하는 기능을 정의합니다.

## 학습 결과

- **car_racing_result.gif**:  
  DQN 학습 후 CarRacing-v2 환경에서 실행한 결과입니다.
