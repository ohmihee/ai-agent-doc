from examples import generate_summary, analyze_image_url
# 폴더 하위에 __init__.py 파일을 통해 내보내주는 경우 파일명 생략하고 바로 import 할 수 있다.

# from examples.generate import generate_summary
# 패키지 하위에 있는 파일을 가져오려면 .사용

# import examples.generate as generate
# 파일 자체를 가져오는 경우 위와 같이 별칭을 사용
    
if __name__ == "__main__":
    # result = generate_summary("파이썬 파일이 실행될 때, 파이썬은 내부적으로 __name__이라는 변수에 이름을 붙여줍니다. 파일을 직접 실행하면 그 이름은 자동으로 __main__이 됩니다.다른 파일에서 도구로 불러오면 그 이름은 파일의 이름이 됩니다.")
    result = analyze_image_url()
    print(result)
    
# 파이썬 파일이 실행될 때 파이썬은 내부적으로 __name__ 이라는 변수에 이름을 붙인다.
# 파일을 직접 실행하면 그 이름은 자동으로 __main__ 이 된다.
# 다른 파일에서 도구로 불러오면 그 이름은 파일의 이름이 된다.
# 즉 위의 코드를 내가 해당 파일을 직접 실행했을 때만 작동하고, 다른 곳에서 불러와 사용했을 때는 실행되지 않도록 제약을 둔 것이다.