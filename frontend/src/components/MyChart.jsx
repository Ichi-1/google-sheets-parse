import React, { useState, useEffect } from 'react';
import { useFetch } from 'hooks/useFetch';
import OrderService from 'api/OrderService';
import { Line } from 'react-chartjs-2';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js'

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
)

export const DemoLine = () => {
    const [dates, setDates] = useState([]);
    const [values, setValues] = useState([]);

    const [fetchOrders, isLoading, error] = useFetch(async () => {
        const response = await OrderService.getChartData()
        const json = await response.json()
        
        const dates_array = json.results.map(k => k['supply_date'])
        const values_array = json.results.map(k => k['value_usd'])

        setDates(dates_array)
        setValues(values_array)
    })


    useEffect(() => {
        const interval = setInterval(() => {
          fetchOrders();
        }, 2000);
        return () => clearInterval(interval);
    }, [dates, values]);
    
    
    return (
        <Line
            datasetIdKey='id'
            data={{
                labels: dates,
                datasets: [
                {
                    id: 1,
                    label: 'order value in USD',
                    data: values,
                },

            ],}}
        />
      
       

    )

};
