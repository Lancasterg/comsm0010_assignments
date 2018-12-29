package io.openvidu.js.java;
import com.amazonaws.services.cognitoidentity.*;
import org.json.simple.parser.ParseException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpSession;

@RestController
@RequestMapping("/api-signup")
public class CognitoSignup {

    @RequestMapping(value = "/signup", method = RequestMethod.POST)
    public ResponseEntity<Object> login(@RequestBody String userPass, HttpSession httpSession) throws ParseException {


        return new ResponseEntity<>(HttpStatus.OK);
    }




}
