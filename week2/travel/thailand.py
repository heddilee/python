class ThailandPackage:
    def detail(self):
        print("[태국 3박 5일 패키지]")

if __name__ == "__main__":
    print("태국 모듈을 직접 실행")
    print("모듈을 직접 실행할 때만 실행됨")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("태국 외부에서 모듈 호출")