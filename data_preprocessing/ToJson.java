package com.yes24.crawler;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ToJson {

    // 메서드
    public static void main(String[] args){
        ToJson toJson = new ToJson();

        ArrayList<HashMap<String, String>> result = new ArrayList<>();
        //HashMap<String, String> temp = new HashMap<>();

        ArrayList<String> values = new ArrayList<>();
        values.add("1");
        values.add("2");
        values.add("3");

        for(int i=0; i< values.size(); i++) {
            HashMap<String, String> temp = new HashMap<>();
            System.out.println(values.get(i));
            temp.put("name", values.get(i));
            result.add(temp);
        }

        System.out.println(result);
/*

        Map<String, String> quiz1 = new HashMap(temp);

//      Map<Integer, String> quiz1 = new LinkedHashMap();
//          만약 여기서 LinkedHashMap으로 만들게 되면
//          연결된 노드들에 의해서 출력도 주입 순서와
//          똑같이 나오게 된다
//          여기서 말하는 출력이란 print 뿐만이 아니라
//          아래 ArrayList에 들어가는 절차도 포함한다

        quiz1.put("1", "프랑스");
        quiz1.put("2", "한국");
        quiz1.put("3", "미국");
        quiz1.put("4", "아랍에미리트");
        quiz1.put("5", "일본");

        for(int i=0; i< quiz1.size(); i++) {
            List<Map> list1 = new ArrayList(quiz1.values());
            System.out.print(list1);
        }

        List<String> list1 = new ArrayList<>();
        list1.add("hi");
        list1.add("yoojin");
*/




    }

    // 생성자
    public ToJson() {

    }

}

