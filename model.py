import cohere
from cohere.classify import Example

def get_destination(apikey, user_input):
    co = cohere.Client(apikey)
    response = co.classify(
          model='bda0f387-8a9a-4a9a-96fd-9e92bceca07b-ft',
          inputs=[user_input])
    return response.classifications[0]       
# print('The confidence levels of the labels are: {}'.format(response.classifications))

def sort_confidence(confidence):
    confidence.sort(key=lambda x: x.confidence)
    confidence.reverse()

