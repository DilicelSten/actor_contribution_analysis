# coding=utf-8
"""
created on:2017/11/1
author:DilicelSten
target:使用pyltp对电影评论进行人名识别，后结果每部电影一个txt，每个人名一行
finished on:2017/11/1
"""
import os
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer


def read_comment():
    """
    读取2017年度所有电影的评论并且存于字典中
    :return:　电影评论字典
    """
    movie_comment = {}
    path = 'D:\Python code\BigHomework\data\comment\\'
    filename = os.listdir(path)
    for each in filename:
        each_comment = []
        file_path = path + each
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                each_comment.append(line)
        movie_comment[each.strip('.txt')] = each_comment
    return movie_comment


def word_splitter(sentence):
    """
    分词
    :param sentence:
    :return:
    """
    segmentor = Segmentor()  # 初始化实例
    segmentor.load('D:\Python code\ltp_model\ltp_data_v3.4.0\cws.model')  # 加载模型
    words = segmentor.segment(sentence)  # 分词
    words_list = list(words)
    segmentor.release()  # 释放模型
    return words_list


def word_tag(words):
    """
    词性标注
    :param words: 已切分好的词
    :return:
    """
    postagger = Postagger()  # 初始化实例
    postagger.load('D:\Python code\ltp_model\ltp_data_v3.4.0\pos.model')  # 加载模型
    postags = postagger.postag(words)  # 词性标注
    postagger.release()  # 释放模型
    return postags


def name_recognition(words, postags):
    """
    命名实体识别
    :param words:分词
    :param postags:标注
    :return:
    """
    recognizer = NamedEntityRecognizer()  # 初始化实例
    recognizer.load('D:\Python code\ltp_model\ltp_data_v3.4.0\\ner.model')  # 加载模型
    netags = recognizer.recognize(words, postags)  # 命名实体识别
    recognizer.release()  # 释放模型
    return netags


def actor_ner(key):
    """
    对每一个评论进行处理
    :param sentence: 影评
    :return: 人名
    """
    result = []
    write_path = 'D:\Python code\BigHomework\data\single_ltp\\'
    movie_comment = read_comment()[key]
    # total_comment = ""
    # with open(write_path + key + '.txt', 'w') as f:
    #     for i in range(len(movie_comment)):
    #         total_comment += movie_comment[i]
    #     total_comment = total_comment.strip('\n')
    #     print total_comment.strip('\n')
    #     words = word_splitter(total_comment)
    #     tags = word_tag(words)
    #     ntags = name_recognition(words, tags)
    #     for word, ntag in zip(words, ntags):
    #         if(ntag == 'S-Nh'):
    #             if(word not in result):
    #                 print word
    #                 result.append(word)
    #                 f.write(word+'\n')
    #                 f.flush()
    with open(write_path + key + '.txt', 'w') as f:
        for i in range(len(movie_comment)):
            words = word_splitter(movie_comment[i])
            tags = word_tag(words)
            ntags = name_recognition(words, tags)
            for word, ntag in zip(words, ntags):
                if(ntag == 'S-Nh'):
                    if(word not in result):
                        print word
                        result.append(word)
                        f.write(word+'\n')
                        f.flush()
        f.close()


if __name__ == '__main__':
    path = 'D:\Python code\BigHomework\data\\new\\'
    filename = os.listdir(path)
    for each in filename:
        print each
        actor_ner(each.strip('.txt'))
        print 'ok'
