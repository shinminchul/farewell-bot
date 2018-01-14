def make_response(answer, keyboard="text", buttons=[]):
    """
    플러스 친구 API의 message 생성기 
    :param answer: 어떤 답변을 해줄 것인지
    :param keyboard: 키보드 타입을 어떤것을 쓸것인지
    :param buttons: 키보드 타입이 버튼이라면 어떤 버튼이 있는가?
    :return: dataSend(추후 jsonfy로 전달될 메세지)
    """
    dataSend = {"message": {"text": answer}, "keyboard": {"type": "text"}}
    if keyboard == "button":
        dataSend["keyboard"]["type"] = "buttons"
        dataSend["keyboard"]["buttons"] = buttons
        return dataSend
    else:
        return dataSend