import requests
from datetime import datetime
import os

def update_readme_with_dog():
    # RandomDog API 호출
    url = "https://random.dog/woof.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        dog_url = data['url']
        
        # 파일이 동영상(.mp4)일 경우 마크다운에서 재생이 안 될 수 있으므로 체크 (선택 사항)
        if dog_url.endswith(('.mp4', '.webm')):
            # 동영상일 경우 다른 사진을 위해 재시도하거나, 일단 링크로 남김
            content_to_add = f"### {datetime.now().strftime('%Y-%m-%d %H:%M')}의 강아지 (비디오)\n[강아지 보기]({dog_url})\n\n---\n"
        else:
            content_to_add = f"### {datetime.now().strftime('%Y-%m-%d %H:%M')}의 강아지\n![dog]({dog_url})\n\n---\n"

        # README.md 파일에 추가
        with open("README.md", "a", encoding="utf-8") as f:
            # 파일이 처음 생성되는 경우를 대비해 상단 제목 추가 (파일이 비어있을 때만)
            if os.path.getsize("README.md") == 0 if os.path.exists("README.md") else True:
                f.write("# 🐶 매일 새로운 강아지 로그\n\n")
            f.write(content_to_add)
            
        print(f"README.md 업데이트 완료: {dog_url}")
        
    except Exception as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":
    update_readme_with_dog()