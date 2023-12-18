from access_llm import llm_answer
from extract_answer import answer_extract

FILE_PATH = "./input_example.txt"


def process_input(file_path):
    """
    Input document path, output (id,question) list
    :param file_path:
    :return: questions_list
    """
    questions_list = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.split('<newline>')
            for line in lines:
                # 分割每一行，得到问题ID和问题文本
                question_id, question_text = line.strip().split('<TAB>', 1)
                # 添加到列表中
                questions_list.append((question_id, question_text))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return questions_list


def intelli_verify(questions_list):
    """
    <ID question><TAB>[R,A,C,E]<answer> where
    "R" indicates the raw text produced by the language model,
    "A" is the extracted answer,
    "C" is the tag correct/incorrect
    "E" are the entities extracted.
    :param questions_list:
    :return:
    """
    for (question_id, question) in questions_list:
        result = ""
        R = llm_answer(question)  # 大语言模型生成的答案
        A = answer_extract(question, R)  # 答案抽取，一个实体或yes/np
        C = fact_check(question, R, A)  # 喜同部分，返回"correct"或"incorrect"
        E = entities_extract(question, R)  # 天宜部分，返回的是一个list，list中元素为元组(entity，wiki_link)




