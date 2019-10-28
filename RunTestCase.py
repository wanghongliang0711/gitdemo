import sys
import pytest
from configure.conf import ROOT_DIR, HTML_NAME

def main():
    if ROOT_DIR not in sys.path:
        sys.path.append(ROOT_DIR)
    # 执行用例
    args = ['--html=' + './report/' + HTML_NAME , "--self-contained-html","-s","-v"]
    pytest.main(args)

if __name__ == '__main__':
    main()







