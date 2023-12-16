from AIs.OpenAI.tools.TIME import ToolTime
from AIs.OpenAI.tools.WTTR_IN import ToolWttrIn
from AIs.OpenAI.tools.WWW_GARINASSET_COM import ToolWwwGarinassetCom
from config.setting import OPENAI_TOOLS_CONFIG
from models.ModelResponse import ResponseTool


class AIOpenAITools:

    @staticmethod
    def get_tools() -> list:
        tools = []
        for tool_config in OPENAI_TOOLS_CONFIG:
            if tool_config["enable"]:
                tool_class = tool_config["Tool"]
                tools.append(tool_class.TOOL_MODEL)
        return tools

    @staticmethod
    def handle(name_tool_call: str, parameter_variables) -> ResponseTool:
        """1、处理路由OpenAI响应的function.name决定。"""
        """2、工具函数参数及变量值也是由OpenAI响应决定，需要具体工具具体相应处理。"""
        match name_tool_call:
            # 1.宏微观经济数据、行业数据、消费品市场价格数据工具-处理
            case ToolWwwGarinassetCom.get_indicator_overview.__name__:
                region = parameter_variables.get("region")
                name = parameter_variables.get("name")
                toolResponse = ToolWwwGarinassetCom.get_indicator_overview(region=region, name=name)
                return toolResponse
            # 2.天气工具-处理
            case ToolWttrIn.get_weather.__name__:
                location = parameter_variables.get("location")
                toolResponse = ToolWttrIn.get_weather(location=location)
                return toolResponse
            case ToolTime.get_time.__name__:
                location = parameter_variables.get("location")
                offset_hours = parameter_variables.get("offset_hours")
                toolResponse = ToolTime.get_time(location=location, offset_hours=offset_hours)
                return toolResponse