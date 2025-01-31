import aiohttp


class ApiExecutor:
    def __init__(self, api_key: str, api_link: str):
        self.__api_key = api_key
        self.__api_link = api_link

    @staticmethod
    def __find_with_true_imei(imei: str, response: list) -> list:
        """Так как api, указанное для тестового задания, возвращало все телефоны,
         а не один конкретный, пришлось делать отдельный метод"""
        print(imei)
        true_phones = [i for i in response if i["deviceId"] == imei]
        print(true_phones)
        return true_phones

    async def check_imei(self, imei: str) -> list:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.__api_link, headers={'Authorization': f'Bearer {self.__api_key}'}, json={'serviceId': 0, 'deviceId': imei}) as response:
                phone = ApiExecutor.__find_with_true_imei(imei, await response.json())
                return phone