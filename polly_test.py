import boto3


def request_from_polly(text):
    try:
        polly_client = boto3.Session(
            aws_access_key_id='AKIA5EGHW7F5RPWAH5FW',
            aws_secret_access_key='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',
            region_name='us-west-2').client('polly')

        response = polly_client.synthesize_speech(VoiceId='Zhiyu',
                                                  OutputFormat='json',
                                                  # Text='轻轻的我走了，正如我轻轻的来，我挥一挥衣袖，不带走一片云彩',
                                                  Text=text,
                                                  SpeechMarkTypes=['viseme', 'word', 'sentence'],
                                                  Engine='standard')

        file = open('alignment.json', 'wb')
        file.write(response['AudioStream'].read())
        file.close()
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    # text = ""
    text = input("Input text of speech: ")
    request_from_polly(text)
