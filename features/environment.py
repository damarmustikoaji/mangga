#untuk lihat semua step definitions
#behave -f steps --dry-run features/

import os, time
#import faker, splinter

from behave.log_capture import capture

from selenium import webdriver
from browser import Browser
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

def before_all(context):

    # Add fake factory
    #context.fake = faker.Faker()

    # Add logging
    context.config.setup_logging()

    context.browser = Browser()
    context.home_page = HomePage()
    context.search_results_page = SearchResultsPage()

    # Dir to output test artifacts
    context.artifacts_dir = 'capture'

def before_feature(context, feature):
    if "skip" in feature.tags:
        feature.skip("Marked with @skip")
        return
    # Whatever other things you might want to do in this hook go here.

def before_scenario(context, scenario):
    if "skip" in scenario.effective_tags:
        scenario.skip("Marked with @skip")
        return
    # Whatever other things you might want to do in this hook go here.

def after_step(context, scenario):
    # Take screenshot if scenario fails
    if scenario.status == 'failed':
        scenario_error_dir = os.path.join(context.artifacts_dir, 'feature_errors')
        make_dir(scenario_error_dir)
        scenario_file_path = os.path.join(scenario_error_dir, scenario.name.replace(' ', '_')
                                          + '_' + time.strftime("%H%M%S_%d_%m_%Y")
                                          + '.png')
        context.browser.driver.save_screenshot(scenario_file_path)#(scenario_file_path)
        context.scenario.skip(reason='karena gagal sebelumnya')
        #context.browser.quit()

def make_dir(dir):
    """
    Checks if directory exists, if not make a directory, given the directory path
    :param: <string>dir: Full path of directory to create
    """
    if not os.path.exists(dir):
        os.makedirs(dir)

def after_all(context):
    #context.browser.close()
    context.browser.quit()
