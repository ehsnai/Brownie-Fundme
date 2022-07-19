from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN


def deploy_fund_me():
    account = get_account()
    # pass price feed adress to fundmme contract

    # if we are on a prestent netwoek like rinkbey, use  associated address otherwise, deploy mocks

    if network.show_active() not in LOCAL_BLOCKCHAIN:
        price_feed_adress = config["networks"][network.show_active()]["bnb_usdt"]
    else:
        deploy_mocks()
        price_feed_adress= MockV3Aggregator[-1].address
    
    fund_me = FundMe.deploy(price_feed_adress,{"from" : account},publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()