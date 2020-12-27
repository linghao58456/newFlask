"""
@author: hao.ling
@Date: 2020/11/21 9:45 下午
@Annotation: 运行服务
"""

from myPlatform.config.service import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9990, debug=True)
