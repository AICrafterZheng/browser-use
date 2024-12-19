import base64
from math import log
import pytest

from browser_use.browser.browser import Browser, BrowserConfig, BrowserContext
from browser_use.agent.views import ActionModel

from browser_use.controller.service import Controller
from browser_use.controller.views import GoToUrlAction
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import asyncio

# @pytest.fixture
# async def browser():
# 	browser_service = Browser(config=BrowserConfig(headless=True))
# 	yield browser_service

# 	await browser_service.close()


# @pytest.mark.skip(reason='takes too long')
# @pytest.mark.asyncio
async def test_take_full_page_screenshot(browser: Browser):
	# Go to a test page
	# browser.go_to_url('https://aicrafter.info')
	browser_context = BrowserContext(browser=browser)
	try:
		controller = Controller()
		action_model = controller.registry.create_action_model()
		# print(f"action_model: {action_model}")
		action_model.go_to_url = GoToUrlAction(url='https://aicrafter.info')
		# print(f"action_model 2: {action_model}")
		# Log registered actions
		print("Registered actions:")
		for action_name in controller.registry.registry.actions:
			print(f"- {action_name}")
		# # Create the GoToUrlAction
		go_to_url_action = GoToUrlAction(url='https://aicrafter.info')
		action_model = ActionModel(
            go_to_url=GoToUrlAction(url='https://aicrafter.info'),
        )
		print(f"action_model 3: {action_model}")
		result = await controller.act(go_to_url_action, browser_context)
		print(f"Result: {result}")
		# Take full page screenshot
		screenshot_b64 = await browser_context.take_screenshot(full_page=True)
		
		# # Verify screenshot is not empty and is valid base64
		# assert screenshot_b64 is not None
		# assert isinstance(screenshot_b64, str)
		# assert len(screenshot_b64) > 0
		
		# save screenshot to file
		with open('screenshot.png', 'wb') as f:
			f.write(base64.b64decode(screenshot_b64))
	except Exception as e:
		print(f'Failed to take screenshot: {str(e)}')
		# pytest.fail(f'Failed to decode base64 screenshot: {str(e)}')
	finally:
		# Explicitly close the browser context
		await browser_context.close()





if __name__ == '__main__':
    print('Running test_take_full_page_screenshot()')
    asyncio.run(test_take_full_page_screenshot(Browser(config=BrowserConfig(headless=False))))
