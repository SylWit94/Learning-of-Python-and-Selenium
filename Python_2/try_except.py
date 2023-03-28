# a = 1
# b = 0
#
# try:
#     result = a/b
#     print(result)
# except:
#     print("Error!")
import selenium.common
# x = 9
# y = 0
#
# try:
#     result = x / y
#     print(result)
# except:
#     print("This is not allowed")

# a = 1
# b = 0
#
# try:
#     result = a/b
#     print(result)
# except ZeroDivisionError as zero_error:
#     print(zero_error)
#     print("Error! ZeroDivisionError")

# nominator = 100.21
# denominator = "a string"
# # denominator = 0
# # denominator = 2
#
# try:
#     result = nominator/denominator
#     print(result)
# except ZeroDivisionError as zero_error:
#     print(zero_error)
#     print("Error! ZeroDivisionError.")
# except TypeError as division_float_string:
#     print(division_float_string)
#     print("An exception TypeError occurred!")
# else:
#     print(result)
#     print("No errors!")
# finally:
#     print("I'm always here")


# def calculate_percent(value, total):
#     try:
#         percent = value * 100 / total
#     except TypeError as string_error:
#         # print(string_error)
#         print("Invalid values! {value} and {total} must be a valid number!")
#     except ZeroDivisionError as zero_error:
#         # print(zero_error)
#         print(f"Invalid values! {value} and {total} must be a valid number!")
#     else:
#         # print("No errors!")
#         print(percent)
#
#
# calculate_percent(1, 2)
# calculate_percent('1', 2)
# calculate_percent('a', None)
# calculate_percent(28, 0)
# calculate_percent(50, 99)


# try except in try except block construction
# a = 0
# b = 1
#
# try:
#     result = a/b
#     print(result)
# except ZeroDivisionError as zero_error:
#     print(zero_error)
#     print("Error! ZeroDivisionError!")
# except TypeError as type_error:
#     print(type_error)
#     print("Error! TypeError!")
# else:
#     try:
#         result = b/a
#         print(result)
#     except:
#         print("No result")
# finally:
#     print("I'm always here")


# # Exercise try except with xpath list
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome(service=Service(r'C:\TestFiles\New_driver\chromedriver.exe'))
# driver.get('https://antoogle.testoneo.com')
#
# xpath_list = ['*yolo_this_is_not_xpath*', '//*[@class="this xpath cannot be found"]',
#               '//*[@class="h6 mb-3 font-weight-normal"]']
#
# for xpath in xpath_list:
#     try:
#         elem = driver.find_element(By.XPATH, xpath)
#         # print(elem.text)
#     except selenium.common.exceptions.InvalidSelectorException as invalid_selector_exceptions:
#         print(invalid_selector_exceptions)
#         print(f'XPath {xpath} is broken!')
#     except selenium.common.exceptions.NoSuchElementException as no_such_element_exception:
#         print(no_such_element_exception)
#         print(f'Element with {xpath} not found')
#     else:
#         print(f'XPath {xpath} is fine and element was found - good job!')
#
# driver.quit()


# # Calculator project with raise Exception
# class Calculator(object):
#     def multiply(value_1, value_2):
#         return value_1 * value_2
#
#     def add(value_1, value_2):
#         return value_1 + value_2
#
#     def divide(value_1, value_2):
#         raise NotImplementedError('Not implemented yet!')
#
#
# print(Calculator.multiply(2, 6))
# print(Calculator.add(2, 6))
# print(Calculator.divide(2, 6))


# Raise in practice
def unsafe_calculate_percent(value, total):
    try:
        return value * 100 / total
    except TypeError:
        raise ValueError(f'Invalid values! {value} and {total} must be a valid number!')
    except ZeroDivisionError:
        raise ValueError(f'Invalid values! {value} and {total} must be a valid number!')


def safe_calculate_percent(value, total):
    try:
        percent = unsafe_calculate_percent(value, total)
    except ValueError as value_error:
        print(value_error)
    else:
        print(f'{value} from {total} is {percent}%')


safe_calculate_percent(1, 2)
safe_calculate_percent('1', 2)
safe_calculate_percent('a', None)
safe_calculate_percent(28, 0)
safe_calculate_percent(50, 99)