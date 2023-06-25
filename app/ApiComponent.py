from qrlib.QRComponent import QRComponent
import requests
from qrlib.QREnv import QREnv
from qrlib.QRRunItem import QRRunItem
from qrlib.QRComponent import QRComponent
import Constants
from robot.libraries.BuiltIn import BuiltIn


class APIComponent(QRComponent):
    def __init__(self):
        super().__init__()

    def load_vault_api(self):
        logger = self.run_item.logger
        logger.info("Accessing vault data for apis")
        self._authorization =  QREnv.VAULTS['authorization']['authorization']
        self._middleware_base_url = QREnv.VAULTS['urls']['middleware_url']
        logger.info("Vault data for APIs accessed successfully")    
   
    def get_data(self, endpoint):
        logger = self.run_item.logger
        logger.info("Calling API")
        response = requests.get(
            f"{self._middleware_base_url }{endpoint}",
            timeout=30,
            headers={
                'Authorization': self._authorization
                },
            )
        data = response.json()
        results = data["results"]
        logger.info(f"API  called successfull")
        return results 
    
    # def update_data(self, response, bot_remark, err=False):
    #     completed_at = BuiltIn().get_time()
    #     bot_status = Constants.ERROR_STATUS if err else Constants.SUCCESS_STATUS
    #     url=f'{self._middleware_base_url }StatusUpdate?BotName={Constants.BOT_NAME}&TableName={response["TABLE_NAME"]}&TableRowId={response["TABLE_ROW_ID"]}&BotCompletedDate={completed_at}&BotCompletedStatus={bot_status}&BotRemarks={bot_remark}&AdditionalRemarks={str(response)}'
    #     headers={'Authorization': self._authorization}
    #     try:
    #         status_update_response = requests.get(url=url, headers=headers)
    #         res = status_update_response.json()
    #         self.logger.info(f"Response from server => {res}")
    #         response = {*response, *res}
    #         report_data = {**response, "Remarks": bot_remark}
    #     except Exception as e:
    #         raise e
        
    # def update_api_test(self, response, bot_remark, err=False):
    #     logger = self.run_item.logger
    #     logger.info(f"Bot remark is {bot_remark}")
    #     logger.info(f"Response is {response}")
    #     bot_status = Constants.ERROR_STATUS if err else Constants.SUCCESS_STATUS
    #     url = f'{self._middleware_base_url}UpdateServiceRequest/UpdateService'
    #     headers={'Authorization': self._authorization}
    #     post_data = {
    #         "Id" : response["ID"],
    #         "BotCompletedStatus" : bot_status,
    #         "BotRemarks" : bot_remark,
    #         "AdditionalRemarks": str(response)
    #     }
    #     logger.info(f"postdata is {post_data}")
    #     logger.info("calling api")
    #     status_update_response = requests.post(url=url, headers=headers, data=post_data)
    #     logger.info("RESPONSE FROM API")
    #     logger.info(status_update_response.text)