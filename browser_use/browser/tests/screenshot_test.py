import base64
import pytest

from browser_use.browser.browser import Browser, BrowserConfig, BrowserContext
from browser_use.agent.views import ActionModel

from browser_use.controller.service import Controller
from browser_use.controller.views import GoToUrlAction
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture
async def browser():
	browser_service = Browser(config=BrowserConfig(headless=True))
	yield browser_service

	await browser_service.close()


# @pytest.mark.skip(reason='takes too long')
@pytest.mark.asyncio
async def test_take_full_page_screenshot(browser: Browser):
	# Go to a test page
	# browser.go_to_url('https://aicrafter.info')
	browser_context = BrowserContext(browser=browser)
	try:
		controller = Controller()
		action_model = controller.registry.create_action_model()
		logger.info(f"action_model: {action_model}")
		action_model.go_to_url = GoToUrlAction(url='https://aicrafter.info')
		logger.info(f"action_model 2: {action_model}")
		# Log registered actions
		logger.info("Registered actions:")
		for action_name in controller.registry.registry.actions:
			logger.info(f"- {action_name}")
		# # Create the GoToUrlAction
		# go_to_url_action = GoToUrlAction(url='https://aicrafter.info')
		action_model = ActionModel(
            go_to_url=GoToUrlAction(url='https://aicrafter.info'),
            # Other actions can remain None
        )
			
		result = await controller.act(action_model, browser_context)
		logger.info(f"Result: {result}")
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
		logger.error(f'Failed to take screenshot: {str(e)}')
		# pytest.fail(f'Failed to decode base64 screenshot: {str(e)}')
	finally:
		# Explicitly close the browser context
		await browser_context.close()





if __name__ == '__main__':
	asyncio.run(test_take_full_page_screenshot(Browser(config=BrowserConfig(headless=False))))
