import 'styles/App.css';
import styled from 'styled-components';
import { DemoLine } from 'components/MyChart';
import { useFetch } from 'hooks/useFetch';
import { useEffect, useState } from 'react';
import OrderService from 'api/OrderService';
import { MyTable } from 'components/MyTable';
const Header = styled.div`
    
    img {
        width: 100px;
        height: 100px;
        float: left;
        margin: 20px
    }
    height: 130px;
    background-color: #3ad082;
    width: 100%;
`

const Main = styled.div`
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    height: 85%;
    width: 130vw;
`;

const SubLeft = styled.div`
    width: 40%;
    height: 100%;
    border: 2px solid gold;
`;

const SubRight = styled.div`
    display: flex;
    width: 39%;
    height: 100%;
    border: 2px solid gold; 
    justify-content: center;
    
`;

const TotalCount = styled.div`
    width: 450px;
    height:200px;
    background-color: #626161;

    h2 {
        padding: 0;
        margin: 0;
        color: #fff;
        text-transform: uppercase;
        
    }

    h1 {
        padding: 0;
        margin: 0;
        color: #fff;
        font-size: 100px;
    }
`;


export const App = () => {
    const [total, setTotal] = useState([])
    const [fetchTotalCount, isLoading, error] = useFetch(async () => {
        const response = await OrderService.getTotalCount()
        const json = await response.json()
        setTotal(json['value_usd__sum'])
    })

    useEffect(() => {
        const interval = setInterval(() => {
            fetchTotalCount();
        }, 2000);
        return () => clearInterval(interval);
    }, []);

    return (
        <div className="App">
            <Header>
                <img src='https://www.designfreelogoonline.com/wp-content/uploads/2021/08/000810-05.png'></img>
            </Header>

            <Main>
                <SubLeft>
                    <DemoLine />
                </SubLeft>
                <SubRight>
                    <TotalCount>
                        <h2>Total Count</h2>
                        <h1>{total}</h1>
                        <div style={{marginTop:'50px', width:'599px'}}>
                            <MyTable />

                        </div>
                    </TotalCount>
                </SubRight>
            </Main>

        </div>
    );
}