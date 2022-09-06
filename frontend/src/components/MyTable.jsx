import { useState, useEffect } from 'react';
import { useFetch } from 'hooks/useFetch';
import OrderService from 'api/OrderService';
import Table from 'rc-table'


export const MyTable = () => {
    const [data, setData] = useState([])
    const [fetchOrders, isLoading, errors] = useFetch(async () => {
        const response = await OrderService.getOrders()
        const json = await response.json()
        setData(json.results)
    })

    const columns = [
        {
            title: '#',
            dataIndex: 'index',
            key: 'index',
            width: 100,
        },
        {
            title: 'order_number',
            dataIndex: 'order_number',
            key: 'order_number',
            width: 100,
        },
        {
            title: 'Value, $',
            dataIndex: 'value_usd',
            key: 'value_usd',
            width: 200,
        },
        {
            title: 'Supply Date',
            dataIndex: 'supply_date',
            key: 'supply_date',
            width: 200,
        },
        {
            title: 'Value, RUB',
            dataIndex: 'value_rub',
            key: 'value_rub',
            width: 200,
        },
    ];


    useEffect(() => {
        const interval = setInterval(() => {
            fetchOrders();
        }, 5000);
        return () => clearInterval(interval);
    }, []);

    return (
        <div style={{ height: 400, width: '100%' }}>
            <Table
                data={data}
                columns={columns}
            />
        </div>
    );
}
