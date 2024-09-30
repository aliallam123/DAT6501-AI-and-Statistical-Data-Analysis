from IPython.display import display, clear_output
from ipywidgets import widgets
from random import shuffle

def create_multipleChoice_widget(description, options, correct_answer):
    if correct_answer not in options:
        options.append(correct_answer)

    shuffle(options)
    correct_answer_index = options.index(correct_answer)
    
    radio_options = [(words, i) for i, words in enumerate(options)]
    alternativ = widgets.RadioButtons(
        options = radio_options,
        description = '',
        layout={'width': 'max-content'},
        disabled = False
    )
    
    description_out = widgets.Output()
    with description_out:
        print(description)
        
    feedback_out = widgets.Output()

    def check_selection(b):
        a = int(alternativ.value)
        if a==correct_answer_index:
            s = '\x1b[6;30;42m' + "Right." + '\x1b[0m' +"\n" #green color
        else:
            s = '\x1b[5;30;41m' + "Wrong. " + '\x1b[0m' +"\n" #red color
        with feedback_out:
            clear_output()
            print(s)
        return
    
    check = widgets.Button(description="submit")
    check.on_click(check_selection)
    
    
    return widgets.VBox([description_out, alternativ, check, feedback_out])
    
Q0=create_multipleChoice_widget('Which of these statements is TRUE', ['Artificial Intelligence is a type of Machine Learning method', 'If I download all of wikipedia on my computer, I would have created artificial intelligence', 'Machine Learning methods require us to explicitely programme models in order to work'], 'Machine Learning methods are used to learn from data without explicit programming')
Q1=create_multipleChoice_widget('Which of these is not an application of Machine Learning?', ['Automatically classify new articles', 'Detecting tumours in brain scans', 'Forecasting the price of apples next year, based on location'], 'List of all the content of the internet')
Q2=create_multipleChoice_widget('Among the following options, identify the one which is not a type of learning?', ['Supervised learning', 'Unsupervised learning', 'Reinforcement learning', 'Semi unsupervised learning'], 'Semi unsupervised learning')
Q3=create_multipleChoice_widget('Identify the type of learning in which labelled training data is used.', ['Supervised learning', 'Unsupervised learning', 'Reinforcement learning'], 'Supervised learning')
Q4=create_multipleChoice_widget('What type of algorithm should you use to allow a robot to walk in various unknown terrains?', ['Supervised learning', 'Unsupervised learning'], 'Reinforcement learning')
Q5=create_multipleChoice_widget('Flagging spam (and ham) in your email box is a type of machine learning method, which one?', ['Batch learning'], 'Online learning')
Q55=create_multipleChoice_widget('What is the purpose of splitting a learning set into train/test sets?', ['To deal with smaller data sets', 'To improve test scores', 'To reduce the number of features used'], 'To avoid being overly optimistic by evaluating\n models on samples that have been used before')


Q6=create_multipleChoice_widget('The decision tree method is an example of:',  ['Reinforcement Learning', 'Unsupervised learning'], 'Supervised learning')
Q7=create_multipleChoice_widget('What is the structure of a decision tree?', ['A graph with a star in the centre and lots of rays', 'A hierarchical list of features and values', 'A network of interconnected neural layers'], 'A linear sequence of nodes with decision rules')
Q8=create_multipleChoice_widget('What is the purpose of splitting nodes in a decision tree?', ['To increase the overall depth of the tree', 'To maximise the entropy of the data at each node', 'To assign all samples to the same leaf node'], 'To minimise the impurity of the data at each node.')
Q9=create_multipleChoice_widget('What is the advantage of using decision trees for machine learning?', ['They require minimal data pre-processing', 'They are always more accurate than other models', 'They can easily handle complex non-linear relationships'], 'They are highly interpretable and easy to understand')

Q10=create_multipleChoice_widget('The nearest neighbours method is an example of:', ['Model-based learning'], 'Instant-based learning' )
Q11=create_multipleChoice_widget('What is the core principle of k-Nearest Neighbours (kNN)?', ['It assumes data points are organised in clusters with similar neighbours.', 'It calculates the distance between all data points and builds a map for efficient retrieval.', 'It automatically learns the most important features for prediction.'], 'It predicts the class or value of a new data point based on the majority vote of its k nearest neighbours in the training data.')
Q12=create_multipleChoice_widget('What is the role of "k" in kNN?', ['It represents the number of features used for distance calculation', 'It determines the complexity of the KNN model', 'It defines the threshold for classifying a data point'], 'It specifies the number of nearest neighbours considered for prediction.')
Q13=create_multipleChoice_widget('Which metric is commonly used for calculating the distance between data points in kNN?', ['Mean squared error', 'Cross-entropy', 'Jaccard similarity'], 'Euclidean distance')


# Q9=create_multipleChoice_widget('What algorithm would you pick among the following options?', ['The one with the highest training scores', 'The one with the highest test scores', 'The one with the highest difference\n between test and training score'], 'The one with the lowest difference\n between test and training score')
# Q10=create_multipleChoice_widget('Which of the following is the best proxy for the generalisation error of a model?',['Training score','Test score','Training error', 'Test Error'],'Test Error')




                                                                                                                 
                                                                                                                 
                                                                                                                 
                                                                                                                 
                                                                                                                 
                                                                                                                 
                                                                                                                 
                                                                                                                 
                                                                                                                 
                                                                                                                 
                                                                                                                 
                                                                                                                 
                                                                                                                 
